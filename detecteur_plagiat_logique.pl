:- use_module(library(readutil)).
:- use_module(library(lists)).

% --- Partie 1 : Extraction de la signature des prédicats ---

programme_signature(File, Signature) :-
    % Charge le fichier dans la base courante
    consult(File),
    % Récupère tous les prédicats avec nom et arité
    findall(Name/Arity, current_predicate(Name/Arity), Predicates),
    sort(Predicates, Signature).

% --- Partie 2 : Lecture et normalisation des clauses ---

read_clauses(File, Clauses) :-
    open(File, read, Stream),
    read_file(Stream, Clauses),
    close(Stream).

read_file(Stream, []) :-
    at_end_of_stream(Stream), !.
read_file(Stream, [Clause|Rest]) :-
    read_term(Stream, Clause, []),
    read_file(Stream, Rest).

% Normalisation : transforme le prédicat en 'r' et tous les arguments en 'v'
normalize_clause(Clause, Normalized) :-
    Clause =.. [_Head|Args],         % Ignore le nom du prédicat
    normalize_args(Args, NormArgs),
    Normalized =.. [r|NormArgs].

normalize_args([], []).
normalize_args([_|T], [v|Rest]) :-
    normalize_args(T, Rest).

normalize_all([], []).
normalize_all([H|T], [NH|NT]) :-
    normalize_clause(H, NH),
    normalize_all(T, NT).

% --- Partie 3 : Calcul des similarités ---

% Similarité sur la signature (prédicats)
similarity_signature(Sig1, Sig2, Score) :-
    intersection(Sig1, Sig2, Common),
    length(Common, NCommon),
    length(Sig1, N1),
    length(Sig2, N2),
    Max is max(N1, N2),
    (Max =:= 0 -> Score = 0 ; Score is (NCommon / Max) * 100).

% Similarité sur les clauses normalisées
similarity_clauses(NC1, NC2, Score) :-
    intersection(NC1, NC2, Common),
    length(Common, NCommon),
    length(NC1, N1),
    length(NC2, N2),
    Max is max(N1, N2),
    (Max =:= 0 -> Score = 0 ; Score is (NCommon / Max) * 100).

% --- Partie 4 : Fonction principale combinée ---

detecter_plagiat_complet(File1, File2) :-
    % Extraction des signatures
    programme_signature(File1, Sig1),
    programme_signature(File2, Sig2),

    % Lecture et normalisation des clauses
    read_clauses(File1, Clauses1),
    read_clauses(File2, Clauses2),
    normalize_all(Clauses1, NormClauses1),
    normalize_all(Clauses2, NormClauses2),

    % Tri pour comparaison plus fiable
    sort(Sig1, SortedSig1),
    sort(Sig2, SortedSig2),
    sort(NormClauses1, SortedNorm1),
    sort(NormClauses2, SortedNorm2),

    % Calcul des similarités
    similarity_signature(SortedSig1, SortedSig2, ScoreSig),
    similarity_clauses(SortedNorm1, SortedNorm2, ScoreClauses),

    % Combinaison simple des scores (moyenne pondérée ici)
    ScoreGlobal is (ScoreSig + ScoreClauses) / 2,

    % Affichage des résultats
    format("Score similarite signatures : ~2f %~n", [ScoreSig]),
    format("Score similarite clauses normalisees : ~2f %~n", [ScoreClauses]),
    format("Score global de similarite : ~2f %~n", [ScoreGlobal]),

    % Verdict
    (ScoreGlobal > 50 ->
        writeln("Possible plagiat detecte !");
        writeln("Programmes differents ou peu similaires.")).

# Setup for full text search, so I don't forget

https://iniakunhuda.medium.com/postgresql-full-text-search-a-powerful-alternative-to-elasticsearch-for-small-to-medium-d9524e001fe0
https://github.com/char0n/postgresql-czech-fulltext/blob/master/README.md
https://stackoverflow.com/a/45074336 - how to find SK dict files
1) Create extensions needed
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE EXTENSION IF NOT EXISTS unaccent;

2) Create search dict

DROP TEXT SEARCH DICTIONARY sk_ispell CASCADE;
CREATE TEXT SEARCH DICTIONARY sk_ispell (
    TEMPLATE = ispell,
    DictFile = sk_SK,
    AffFile = sk_SK,
    StopWords = czech
);

3) Create search config

CREATE TEXT SEARCH CONFIGURATION slovak( COPY = simple );
ALTER TEXT SEARCH CONFIGURATION slovak
    ALTER MAPPING FOR hword, hword_part, word
    WITH sk_ispell;

4) Create an unmmutable wrapper arround unaccent
CREATE OR REPLACE FUNCTION immutable_unaccent(text)
RETURNS text 
LANGUAGE sql 
IMMUTABLE 
STRICT 
AS $function$
    SELECT unaccent($1)
$function$;

5) Create a cache

ALTER TABLE PUBLIC.SUBJECTS
ADD COLUMN IF NOT EXISTS SEARCH_VECTOR TSVECTOR GENERATED ALWAYS AS (
	SETWEIGHT(TO_TSVECTOR('slovak',IMMUTABLE_UNACCENT (COALESCE(SUBJECTS."name", ''))),'A') ||
	SETWEIGHT(TO_TSVECTOR('simple',IMMUTABLE_UNACCENT (COALESCE(SUBJECTS."aisCode", ''))),'B')
) STORED;

6) Create an index

CREATE INDEX subjects_search_idx ON subjects USING GIN (search_vector);

## Useful queries:

SELECT to_tsvector('simple',unaccent('Manažment bezpečnosti v informačných technológiách'));

SELECT * FROM pg_catalog.pg_ts_dict;

## Final search query:

SELECT 
    *,
    ts_rank(search_vector, query) as rank
FROM 
    subjects,
    to_tsquery('slovak', UNACCENT('programovanie')) query
WHERE search_vector @@ query
ORDER BY rank DESC;
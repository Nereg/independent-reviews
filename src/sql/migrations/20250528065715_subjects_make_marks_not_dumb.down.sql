BEGIN;

ALTER TABLE public.reviews 
    ALTER COLUMN mark DROP NOT NULL;

ALTER TABLE public.reviews 
    ALTER COLUMN mark TYPE integer;

COMMIT;
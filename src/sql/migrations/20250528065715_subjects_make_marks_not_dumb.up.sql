BEGIN;

ALTER TABLE public.reviews
    ALTER COLUMN mark TYPE real;

ALTER TABLE IF EXISTS public.reviews
    ALTER COLUMN mark SET NOT NULL;

COMMIT;
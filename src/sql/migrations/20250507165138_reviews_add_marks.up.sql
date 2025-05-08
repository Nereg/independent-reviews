BEGIN;

ALTER TABLE IF EXISTS public.reviews
    ADD COLUMN mark integer;

END;
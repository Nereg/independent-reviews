BEGIN;

-- First drop all constraints
ALTER TABLE IF EXISTS public.users
    DROP CONSTRAINT IF EXISTS "facultyIdFk";
    
ALTER TABLE IF EXISTS public.telegram
    DROP CONSTRAINT IF EXISTS "userIdFk";
    
ALTER TABLE IF EXISTS public.permissions
    DROP CONSTRAINT IF EXISTS "userIdFk";
    
ALTER TABLE IF EXISTS public.reviews
    DROP CONSTRAINT IF EXISTS "authorFk";
    
ALTER TABLE IF EXISTS public.reviews
    DROP CONSTRAINT IF EXISTS "subjectIdFk";
    
ALTER TABLE IF EXISTS public.reviews
    DROP CONSTRAINT IF EXISTS "practitionerIdFk";
    
ALTER TABLE IF EXISTS public.reviews
    DROP CONSTRAINT IF EXISTS "lectorIdFk";
    
ALTER TABLE IF EXISTS public.subjects
    DROP CONSTRAINT IF EXISTS "facultyIdFk";

-- Then drop all tables
-- Drop in reverse order of dependencies
DROP TABLE IF EXISTS public.telegram;
DROP TABLE IF EXISTS public.permissions;
DROP TABLE IF EXISTS public.reviews;
DROP TABLE IF EXISTS public.users;
DROP TABLE IF EXISTS public.subjects;
DROP TABLE IF EXISTS public.lectors;
DROP TABLE IF EXISTS public.practitioners;
DROP TABLE IF EXISTS public.faculties;

COMMIT;
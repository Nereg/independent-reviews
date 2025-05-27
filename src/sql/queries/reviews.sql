-- name: getReviewById :one
SELECT reviews."id", reviews."author", reviews."subjectId", reviews."text", reviews."deleted", reviews."language", reviews."practitionerId", reviews."subjectRating", reviews."lectorRating", reviews."practitionerRating", reviews."practitionerReview", reviews."lectorReview", reviews."yearBeginning", reviews."timestamp", reviews."mark", subjects."name", subjects."facultyId", subjects."aisid", subjects."stage", subjects."semester", subjects."aisCode"
FROM public.reviews
INNER JOIN public.subjects ON subjects.id = reviews."subjectId"
WHERE reviews."id" = $1;

-- name: getReviewsByIds :many
SELECT reviews."id", reviews."author", reviews."subjectId", reviews."text", reviews."deleted", reviews."language", reviews."practitionerId", reviews."subjectRating", reviews."lectorRating", reviews."practitionerRating", reviews."practitionerReview", reviews."lectorReview", reviews."yearBeginning", reviews."timestamp", reviews."mark", subjects."name", subjects."facultyId", subjects."aisid", subjects."stage", subjects."semester", subjects."aisCode"
FROM public.reviews
INNER JOIN public.subjects ON subjects.id = reviews."subjectId"
WHERE reviews."id" IN ($1);
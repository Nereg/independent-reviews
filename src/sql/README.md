To generate SQLC code:
`docker run --rm -v $(pwd)/src/sql:/src -w /src sqlc/sqlc generate`
If you are on git bash on windows, prepend this: `MSYS_NO_PATHCONV=1`
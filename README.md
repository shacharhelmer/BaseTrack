# BaseTrack

The importance of version control for code is already well-known. There exists many solutions for this - Git being one of the popular ones. 
Not as recognized in many compnies is the need for verison control in database. A Database schema, stored procedures, views, pipelines and replications
are all code snippets that are changed over time. Tracking, reverting, pin-pointing changes could be critical to trouble shooting and could ease development.

This is the point of this product - solving the version control problem for databases while not giving up being light-weight and easy to use.

Currently supported databases:
- MySQL (schema and stored procedures at pre-commit)

Currently supported version control system:
- Git

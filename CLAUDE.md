CLAUDE.md

Project Overview

FastAPI application using Jinja2 and HTMX for the Web UI, SQLAlchemy for database access, Pydantic for schemas and settings, and SQLAdmin for the admin panel.

The project follows a feature-oriented structure with a separation between routing, business logic, data access, and infrastructure.

Architecture

src/
├── main.py             # App factory, lifespan and middleware
├── config.py           # Application settings via pydantic-settings
├── router.py           # Central composition of API and Web routers
├── exceptions.py       # Application exceptions
├── base_dao.py         # Base abstraction for database access
├── base_jinja.py       # Base Jinja configuration and rendering utilities
│
├── web/                # Web UI: routes, Jinja templates, static files and HTMX
├── admin/              # SQLAdmin-based admin panel
│
├── users/              # User domain
│   ├── models.py       # SQLAlchemy database models
│   ├── router.py       # API routes
│   ├── web.py          # Web routes
│   ├── user.py         # User-related functionality
│   ├── schemas.py      # Pydantic request/response schemas
│   ├── dependencies.py # FastAPI dependencies
│   └── service.py      # Business logic
│
└── infrastructure/     # Application infrastructure
    └── database.py     # SQLAlchemy engine and session management

Core Rules

* Inspect existing code and patterns before making changes.
* Follow the existing project architecture.
* Keep route handlers thin.
* Put business logic in service.py.
* Keep database access separate from route handlers.
* Use Pydantic schemas for request/response data.
* Use FastAPI dependencies for dependency injection.
* Keep infrastructure code inside infrastructure/.
* Keep Web UI concerns inside web/.
* Do not introduce new architectural patterns without a clear reason.
* Do not create unnecessary abstractions or files.
* Prefer modifying existing functionality over duplicating it.
* Keep changes focused on the requested task.

Web UI

The Web UI uses:

* Jinja2 for server-side HTML rendering.
* HTMX for dynamic page interactions.
* Static assets under src/web/static/.
* Templates under src/web/templates/.

Templates are responsible for presentation only.

Business logic must remain in the service layer.

Feature Structure

Application functionality should be organized by domain/feature.

For example:

users/
├── models.py
├── router.py
├── web.py
├── user.py
├── schemas.py
├── dependencies.py
└── service.py

When adding a new domain, follow the same structure where applicable.

Do not create files that are not required by the feature.

Request Flow

For API requests:

Router
  ↓
Dependencies
  ↓
Service
  ↓
DAO / Data Access
  ↓
Database

For Web requests:

Web Route
  ↓
Service
  ↓
DAO / Data Access
  ↓
Jinja Template
  ↓
HTML / HTMX

Database

SQLAlchemy is used for database access.

Database engine and session management belong to:

src/infrastructure/database.py

Feature-specific database operations should not be placed directly inside route handlers.

Testing

Tests are located in:

tests/

When changing application behavior:

1. Inspect existing tests.
2. Update affected tests.
3. Add tests for new behavior where appropriate.
4. Run the relevant test suite.

Do not modify tests only to make failing behavior pass.

Code Style

Prefer simple, explicit code over unnecessary abstractions.

Follow the style and conventions already established in the repository.

Do not add comments that merely describe obvious code. Comments should explain non-obvious decisions, constraints, or workarounds.

Before Completing a Task

Verify that:

* The implementation follows the existing architecture.
* No unnecessary files or abstractions were introduced.
* Business logic is not leaking into routes or templates.
* Existing functionality has not been unnecessarily changed.
* Relevant tests pass.
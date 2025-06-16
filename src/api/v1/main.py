# Copyright (c) 2024 Umbra. All rights reserved.
<<<<<<< HEAD
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse

from src.data_engineering.db_utils import check_db_health
from src.utils.logging_utils import setup_logging
from src.api.v1.endpoints import courses, recommendations, users  # Import users router
from src.api.v1.exceptions import (
    DatabaseError,
    NotFoundError,
    ConflictError,
)  # Import custom exceptions
=======
from fastapi import FastAPI, Depends, HTTPException, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List, Dict

from src.data_engineering.db_utils import get_db, check_db_health
from src.data_collection.data_ingestion import ingest_course_data_batch, validate_scraped_data
from src.utils.logging_utils import setup_logging
from src.api.v1.schemas import CourseCreate
from src.api.v1.endpoints import courses, recommendations
from src.api.v1.exceptions import DatabaseError, NotFoundError, ConflictError # Import custom exceptions
>>>>>>> 63e865f (Initial commit: Umbra Educational Data Platform)

# Setup logging for the API
logger = setup_logging(__name__)

app = FastAPI(
    title="Educational Data Science Platform API",
    description="API for managing educational content, learning progress, and recommendations.",
    version="1.0.0",
<<<<<<< HEAD
    root_path="/api/v1",  # Explicitly set the root path for the application
=======
    root_path="/api/v1" # Explicitly set the root path for the application
>>>>>>> 63e865f (Initial commit: Umbra Educational Data Platform)
)

# Include routers for different API functionalities.
app.include_router(courses.router, prefix="/courses", tags=["Courses"])
<<<<<<< HEAD
app.include_router(
    recommendations.router, prefix="/recommendations", tags=["Recommendations"]
)
app.include_router(users.router, tags=["Users"])  # Include the users router

=======
app.include_router(recommendations.router, prefix="/recommendations", tags=["Recommendations"])

# --- Temporary Diagnostic Endpoint ---
@app.get("/get-root-path", summary="Get Application Root Path", tags=["Diagnostics"])
def get_root_path(request: Request):
    """
    Returns the root path as perceived by the FastAPI application at runtime.
    This is a temporary diagnostic endpoint to debug prefixing issues.
    """
    return {"app_root_path": request.scope.get("root_path")}
>>>>>>> 63e865f (Initial commit: Umbra Educational Data Platform)

# --- Global Exception Handlers ---
@app.exception_handler(DatabaseError)
async def database_exception_handler(request: Request, exc: DatabaseError):
    logger.error(f"Database Error occurred: {exc.detail}", exc_info=True)
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail, "code": "database_error"},
    )

<<<<<<< HEAD

=======
>>>>>>> 63e865f (Initial commit: Umbra Educational Data Platform)
@app.exception_handler(NotFoundError)
async def not_found_exception_handler(request: Request, exc: NotFoundError):
    logger.warning(f"Resource not found: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail, "code": "not_found"},
    )

<<<<<<< HEAD

=======
>>>>>>> 63e865f (Initial commit: Umbra Educational Data Platform)
@app.exception_handler(ConflictError)
async def conflict_exception_handler(request: Request, exc: ConflictError):
    logger.warning(f"Conflict error: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail, "code": "conflict_error"},
    )

<<<<<<< HEAD

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.error(
        f"HTTP Exception occurred: {exc.detail} (Status: {exc.status_code})",
        exc_info=True,
    )
=======
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.error(f"HTTP Exception occurred: {exc.detail} (Status: {exc.status_code})", exc_info=True)
>>>>>>> 63e865f (Initial commit: Umbra Educational Data Platform)
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail, "code": "http_error"},
    )

<<<<<<< HEAD

=======
>>>>>>> 63e865f (Initial commit: Umbra Educational Data Platform)
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    logger.critical(f"An unhandled error occurred: {exc}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": "An unexpected error occurred.", "code": "server_error"},
    )
<<<<<<< HEAD


# --- End Global Exception Handlers ---


=======
# --- End Global Exception Handlers ---

>>>>>>> 63e865f (Initial commit: Umbra Educational Data Platform)
@app.get("/health", summary="Health Check", tags=["Monitoring"])
def health_check():
    """
    Performs a health check on the API and its dependencies.
    Returns 200 if the API is up and the database connection is healthy.
    """
    if check_db_health():
        return {"status": "healthy", "database_connection": "successful"}
    else:
        # This will now be caught by the DatabaseError handler if it's a DB issue
        # or a generic HTTPException if check_db_health() raises a different HTTPException
<<<<<<< HEAD
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database connection failed",
        )

=======
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database connection failed")
>>>>>>> 63e865f (Initial commit: Umbra Educational Data Platform)

# Remove redundant ingest-courses endpoint from main.py, as it's defined in courses.py
# @app.post("/ingest-courses", summary="Ingest Course Data", tags=["Data Ingestion"])
# async def ingest_courses(course_data_list: List[CourseCreate], db: Session = Depends(get_db)):
#     """
#     Ingests a list of course data into the database.

#     - **course_data_list**: A list of CourseCreate objects, representing courses to be ingested.
#     """
#     if not course_data_list:
#         raise HTTPException(status_code=400, detail="No course data provided.")

#     valid_data_for_ingestion = [
#         course.dict() for course in course_data_list if validate_scraped_data(course.dict())
#     ]

#     if not valid_data_for_ingestion:
#         raise HTTPException(status_code=400, detail="No valid course data found for ingestion after validation.")

#     try:
#         ingest_course_data_batch(valid_data_for_ingestion, db)
#         return {"status": "success", "message": f"Attempted to ingest {len(valid_data_for_ingestion)} valid courses."}
#     except Exception as e:
#         logger.error(f"API - Error during course ingestion: {e}")
#         raise HTTPException(status_code=500, detail=f"Internal server error during ingestion: {e}")

# You can add more endpoints here for other workflows (e.g., user management, content retrieval, etc.)

# This is a test comment for reload functionality

if __name__ == "__main__":
    import uvicorn
<<<<<<< HEAD

    logger.info("Starting FastAPI application...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
=======
    logger.info("Starting FastAPI application...")
    uvicorn.run(app, host="0.0.0.0", port=8000) 
>>>>>>> 63e865f (Initial commit: Umbra Educational Data Platform)

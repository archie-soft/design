# Archie Design Documents

## REST Services

![services diagram](diagrams/services.png)

### External

- Docs
  - Documents are the main building blocks of the applicaton. Each one combines an Apache Solr document and the file or artifact it describes.
  - Methods
    - Get: Returns all information about a document and usually also the path to the file it desribes.
    - Put: Creates a new document, after validating the file and performing other operations on it, such as extracting text and generating a thumbnail.
    - Patch: Updates a document and optionally to the file it describes.
    - Delete: Deletes both the document and its files.
- Folders: 
    - This service is used in batch import jobs. It present the user a list of pre-existing folders with files that can be sent to the Docs service.
    - Methods
      - Get
      - Delete
- Reports
    - This service displays information about the results of put docs and backup services. It is also consumed by those services when creating the reports.
    - Methods
      - Put
      - Get
- Drafts
  - This service allows the user to view items received automatically from external chanels, like mail, and then deside if he wants to import it to the system (by sending it to the put docs service).
  - Methods
    - Put
    - Get
    - Delete
- Backups
  - This service is triggered by a scheduler. It copies documents and files to a dedicated AWS S3 bucket.
  - Methods
    - Put: performs a backup by calling the Docs and Files services

### Internal

- Files
  - Files (assets) are stored in AWS S3 buckets, according to its access-rights: public, private, secret.
  - Methods
    - Get: Reads a file from an S3 bucket, by concatenating access-rights, id and format from the associated document.
    - Put: Uploads a file to S3 bucket.
    - Patch: Performs various operatons on the file, after it already imported to the system, like: re-generating thumbnail, re-extracting text or converting video file to another format.
    - Delete: Deletes the main asset file from an S3 bucket, together with its related files (content, thumbnail, etc).
- Thumbnails
  - This service generates a small low-resolution image from the main asset file (image, video and pdf files are currently supported).
  - Methods
    - Put
    - Delete
- Content
  - This service extracts or recognize text from a PDF file, or transcript an audio or video file.
  - Methods
    - Put
- Faces
  - This is a face recognition service
  - Methods
    - Put
    - Get

## Code repositories naming conventions

  - xxx-service for REST endpoints (example: docs-service)
  - xxx-lib for common logic that can be used by the services (example: image-manipulaton-lib)
  - free text for special stuff (example: design, infrastructure)

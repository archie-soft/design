# Archie Design Documents

## REST Services

- Docs (Apache Solr documents, each one represent a file or an artifact)
  - Get: Search for an Apache Solr document
  - Put: Creates an Apache Solr document
  - Patch: Updates an Apache Solr document
  - Delete: Deletes an Apache Solr document
- Files (Stored in an AWS S3 buckets, according to its access-rights - public, private, secret)
  - Get: Reads a file from an S3 bucket
  - Put: Uploads a file to S3 bucket
  - Delete: Deletes a file from an S3 bucket
- Folders: Used in batch ingest workflow
- Thumbnails: Small image created from the original image or video or pdf file
- Content: Text extracted from a PDF or generated from speech (recognized) in audio or video file
- Reports: Create and view reports about ingest operations
- Drafts: Received automatically from external chanels, like mail.
- Faces: Face recognition service
- Landmarks: Landmark recognition service
- Backups
  - Get: return information about a backup
  - Put: performs a backup by calling the Docs and Files services

## Workflows

- Ingest: Import data into the system
  - get folders
  - put docs
  - put files
  - put thumbnails
  - put content
  - put reports

## Code repositories types

  - service (REST endpoints)
  - library (common functionality)
  - misc (design, infrastructure)

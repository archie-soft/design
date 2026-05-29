"""
Digital Archive REST API Service
Provides endpoints for managing documents in the archive
"""

from flask import Flask, request, jsonify
from typing import Dict, List, Any
import json

app = Flask(__name__)

# In-memory storage for documents (in production, use a database)
documents: Dict[str, Any] = {}
document_counter: int = 0


@app.route('/api/documents', methods=['GET'])
def get_documents() -> tuple[Dict[str, Any], int]:
    """
    GET /api/documents
    Retrieve all documents from the archive
    
    Returns:
        JSON array of documents with 200 status code
    """
    try:
        docs_list = list(documents.values())
        return jsonify({
            'status': 'success',
            'count': len(docs_list),
            'documents': docs_list
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/documents', methods=['POST'])
def create_document() -> tuple[Dict[str, Any], int]:
    """
    POST /api/documents
    Create a new document in the archive
    
    Expected JSON payload:
    {
        "title": "Document Title",
        "content": "Document content",
        "metadata": {...}
    }
    
    Returns:
        JSON response with created document and 201 status code
    """
    global document_counter
    
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data or 'title' not in data:
            return jsonify({
                'status': 'error',
                'message': 'Missing required field: title'
            }), 400
        
        # Create new document
        document_counter += 1
        doc_id = str(document_counter)
        
        new_document = {
            'id': doc_id,
            'title': data.get('title'),
            'content': data.get('content', ''),
            'metadata': data.get('metadata', {})
        }
        
        documents[doc_id] = new_document
        
        return jsonify({
            'status': 'success',
            'message': 'Document created successfully',
            'document': new_document
        }), 201
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/documents/<doc_id>', methods=['GET'])
def get_document(doc_id: str) -> tuple[Dict[str, Any], int]:
    """
    GET /api/documents/<doc_id>
    Retrieve a specific document by ID
    
    Returns:
        JSON response with document or 404 if not found
    """
    if doc_id in documents:
        return jsonify({
            'status': 'success',
            'document': documents[doc_id]
        }), 200
    else:
        return jsonify({
            'status': 'error',
            'message': f'Document {doc_id} not found'
        }), 404


@app.route('/api/health', methods=['GET'])
def health_check() -> tuple[Dict[str, str], int]:
    """
    GET /api/health
    Health check endpoint
    """
    return jsonify({'status': 'healthy'}), 200


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)

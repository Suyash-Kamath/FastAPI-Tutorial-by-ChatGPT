from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import List

app = FastAPI()

# Serve HTML form
@app.get("/", response_class=HTMLResponse)
def form_ui():
    return """
    <html>
        <head><title>Resume Upload</title></head>
        <body>
            <h2>Resume Upload Form</h2>
            <form action="/analyze-resumes/" enctype="multipart/form-data" method="post">
                <label>Job Description:</label><br/>
                <textarea name="job_description" rows="4" cols="50">We need a sales executive...</textarea><br/><br/>

                <label>Hiring Type:</label>
                <select name="hiring_type">
                    <option value="fresher">Fresher</option>
                    <option value="experienced">Experienced</option>
                </select><br/><br/>

                <label>Experience Level:</label>
                <select name="level">
                    <option value="junior">Junior</option>
                    <option value="mid">Mid</option>
                    <option value="senior">Senior</option>
                </select><br/><br/>

                <label>Upload Resumes:</label>
                <input name="files" type="file" multiple/><br/><br/>

                <input type="submit" value="Submit"/>
            </form>
        </body>
    </html>
    """


# Handle form submission and files
@app.post("/analyze-resumes/")
async def analyze_resumes(
    job_description: str = Form(...),
    hiring_type: str = Form(...),
    level: str = Form(...),
    files: List[UploadFile] = File(...)
):
    result = {
        "job_description": job_description,
        "hiring_type": hiring_type,
        "level": level,
        "uploaded_files": []
    }

    for file in files:
        size = 0
        chunk_count = 0

        while chunk := await file.read(1024):  # Read in 1KB chunks
            chunk_count += 1
            size += len(chunk)

        result["uploaded_files"].append({
            "filename": file.filename,
            "size_kb": round(size / 1024, 2),
            "chunks": chunk_count,
            "content_type": file.content_type
        })

    return result

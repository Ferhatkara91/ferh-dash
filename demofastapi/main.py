from fastapi import fastapi

app=fastapi()

@app.get('/hello')
def hello():
    """Test endpoint"""
    return {'Hello': 'World'}

    
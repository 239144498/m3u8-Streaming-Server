#!/usr/bin python3
# -*- coding: utf-8 -*-

import os
from app import app


if __name__ == '__main__':
    import uvicorn
    print(f'http://127.0.0.1:{int(os.getenv("PORT", default=15000))}')
    # uvicorn.run(app='main:app', host="127.0.0.1", port=15000, reload=True, debug=True)
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", default=15000)), log_level="info")

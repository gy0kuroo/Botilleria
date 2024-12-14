{
    "builds": [
      {
        "src": "build_files.sh",
        "use": "@vercel/static-build",
        "config": {
          "distDir": "staticfiles_build"
        }
      },
      {
        "src": "/czarny_kot/wsgi.py",
        "use": "@vercel/python",
        "config": { "maxLambdaSize": "15mb" }
      }
    ],
    "routes": [
      {
        "src": "/(.*)",
        "dest": "czarny_kot/wsgi.py"
      },
      {
        "src": "/static/(.*)",
        "dest": "/static/$1"
      }
    ]
  }
# scrapper-challenge


To debug your application in vscode, you can use this configuration of launch.json

{
    "version": "0.1.0",
    "configurations": [
        {
            "name": "Python: Launch Scrapy Spider",
            "type": "debugpy",
            "request": "launch",
            "module": "scrapy",
            "args": [
                "runspider",
                "challenge/spiders/istock.py"
            ],
            "console": "integratedTerminal"
        }
    ]
}

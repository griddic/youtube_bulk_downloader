init:
	pip install -r requirements.txt -U
download:
	python downloader.py
clean:
	rm -rf downloads | true

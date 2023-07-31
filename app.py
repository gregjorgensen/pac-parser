from flask import Flask, request, render_template
import pacparser

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    proxy = ''
    error = ''
    if request.method == 'POST':
        pac_script = request.form.get('pac_script')
        url = request.form.get('url')

        # Validate PAC script
        if "function FindProxyForURL" not in pac_script:
            error = "Invalid PAC script"
        else:
            # Initialize pacparser
            pacparser.init()

            # Add "http://" to the URL if necessary
            if not url.startswith(('http://', 'https://')):
                url = 'http://' + url

            try:
                # Parse the PAC script
                pacparser.parse_pac_string(pac_script)

                # Find a proxy for the given URL
                proxy = pacparser.find_proxy(url)
            except Exception as e:
                error = f"Unexpected error: {str(e)}"
            finally:
                # Cleanup after pacparser
                pacparser.cleanup()

    return render_template('index.html', proxy=proxy, error=error, url=url, pac_script=pac_script)

if __name__ == '__main__':
    app.run(debug=True)

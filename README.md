# 🌟 HypeAPI

Unofficial Python module for interacting with the HYPE card API.

![GitHub contributors](https://img.shields.io/github/contributors/MatteoFasulo/HypeBankAPI-dashboard)
[![GitHub issues](https://img.shields.io/github/issues/MatteoFasulo/HypeBankAPI-dashboard)](https://github.com/MatteoFasulo/HypeBankAPI-dashboard/issues)
[![GitHub stars](https://img.shields.io/github/stars/MatteoFasulo/HypeBankAPI-dashboard)](https://github.com/MatteoFasulo/HypeBankAPI-dashboard/stargazers)
![GitHub closed issues](https://img.shields.io/github/issues-closed/MatteoFasulo/HypeBankAPI-dashboard)
![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/MatteoFasulo/HypeBankAPI-dashboard)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/MatteoFasulo/HypeBankAPI-dashboard)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/MatteoFasulo/HypeBankAPI-dashboard)
[![GitHub license](https://img.shields.io/github/license/MatteoFasulo/HypeBankAPI-dashboard)](https://github.com/MatteoFasulo/HypeBankAPI-dashboard)

## 📝 Notes
- HYPE only allows the use of one device at a time. Logging in with this module will disconnect you from the application and vice versa.

## 🐳 Docker
`start.sh` will run the python script and then build the image with all the data generated:
```sh
./start.sh
docker run -p 8501:8501 hype_dashboard
```
Then visit [http://127.0.0.1:8501](http://127.0.0.1:8501) to view the Streamlit app!

## 🚀 Standalone
Run:
```python
git clone https://github.com/MatteoFasulo/HypeBankAPI-dashboard
```
The `main.py` script supports argparse for command line arguments:
```python
python main.py -m EMAIL -b BIRTHDATE [-l LIMIT] [-v]
```
The script is invoked using the following command-line arguments:
- `-m EMAIL`, `--email EMAIL`: Specifies the email address. It is a required argument.
- `-b BIRTHDATE`, `--birthdate BIRTHDATE`: Specifies the birth date. It is a required argument.
- `-l LIMIT`, `--limit LIMIT`: Limit the number of transactions to fetch from Hype API. Default to 50. It is an optional argument.
- `-v`, `--verbose`: Enables verbose output. It is an optional flag argument.
>Tip: If you encountered an error while running the command try `python3 main.py`

In order to run the Streamlit app, you need to run `main.py` and then execute:
```python
streamlit run Home.py --server.port=8501 --server.address=127.0.0.1
```
> 📄 Home.py is the main Streamlit page. The WebApp has multiple pages inside the `pages` folder!

## 💻 Dashboard
### 💸 Movements
![image](https://github.com/MatteoFasulo/HypeAPI/assets/74818541/70a0fb2d-7175-4891-b144-56106ca7ddb4)

### 💳 Card
![image](https://github.com/MatteoFasulo/HypeAPI/assets/74818541/50b6a0f6-d386-4f3b-88b9-1972ac30a194)

<hr>

## ⚠️ Disclaimer
The contents of this repository are for informational purposes and the result of personal research. The author is not affiliated, associated, authorized, endorsed by, or in any way connected with Banca Sella S.p.A., or with its affiliated companies. All registered trademarks belong to their respective owners.

## 🙏 Acknowledgments
- [@jacopo-j/HypeAPI](https://github.com/jacopo-j/HypeAPI) for the API interface.

## Contributing
Thank you for considering contributing to the HypeAPI project! Please read the [Contributing Guidelines](CONTRIBUTING.md) for more information on how to contribute.

## Code of Conduct
We expect all contributors to adhere to the [Code of Conduct](CODE_OF_CONDUCT.md). Please read it to understand the behavior we expect from our community members.

## License
Matteo Fasulo © 2023 - Released under the Apache-2.0 License.
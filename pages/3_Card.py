import os
import base64
from datetime import datetime
from PIL import Image
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Hype Personal Dashboard",
    page_icon="🏠",
    layout='wide',
    initial_sidebar_state='expanded',
    menu_items={
        'Get Help': 'https://github.com/MatteoFasulo/HypeAPI',
        'Report a bug': "https://github.com/MatteoFasulo/HypeAPI/issues",
        'About': 
            """
            # Hype Personal Dashboard
            This webapp was created with the aim of allowing Hype users to better analyze their account through the use of aggregated statistics and graphs.
            Any contribution to this project is welcome to improve the quality of work!

            GitHub Repository: https://github.com/MatteoFasulo/HypeAPI
            """
        }
)

@st.cache_data
def load_card():
    card = pd.read_json('json/card.json', orient='index').transpose()
    card_settings = pd.json_normalize(card['setting'][0]['operations'])
    card_settings.isEnable = card_settings.isEnable.apply(lambda x: 'Enabled' if x else 'Disabled')
    card = card.iloc[0]
    return card, card_settings

@st.cache_data
def random_card_number():
    card_number = ''
    for i in range(16):
        digit = '*'
        card_number += str(digit)
        if (i + 1) % 4 == 0 and i != 15:
            card_number += " "  # Insert a space every four digits
    return card_number

@st.cache_data
def img_to_base64(img):
    with open(f'static{os.sep}img{os.sep}{img}', 'rb') as image_file:
        image_data = image_file.read()
    image_base64 = base64.b64encode(image_data).decode('utf-8')
    with open('text.txt', 'w') as text:
        text.write(image_base64)
    return image_base64

card, card_settings = load_card()
card_manufacturer = 'HYPE'
card_number = random_card_number()
card_expiration = datetime.strptime(card.expirationDate, '%Y-%m-%d')
card_expiration = card_expiration.strftime("%m / %y")
card_expiration = ' '.join(card_expiration)
card_owner = f'{card.firstName} {card.lastName}'

with open(f'static{os.sep}css{os.sep}style.css', encoding='UTF-8') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)

with col2:
    st.markdown(
        f"""
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <svg xml:space="preserve" viewBox="0 0 50 50" height="30px" width="30px" y="0px" x="0px" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" id="Layer_1" class="hype" version="1.1">  <image href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAYUAAAE7CAYAAAAy451NAAAKQWlDQ1BJQ0MgUHJvZmlsZQAASA2dl
                    ndUU9kWh8+9N73QEiIgJfQaegkg0jtIFQRRiUmAUAKGhCZ2RAVGFBEpVmRUwAFHhyJjRRQLg4Ji1w
                    nyEFDGwVFEReXdjGsJ7601896a/cdZ39nnt9fZZ+9917oAUPyCBMJ0WAGANKFYFO7rwVwSE8vE9wI
                    YEAEOWAHA4WZmBEf4RALU/L09mZmoSMaz9u4ugGS72yy/UCZz1v9/kSI3QyQGAApF1TY8fiYX5QKU
                    U7PFGTL/BMr0lSkyhjEyFqEJoqwi48SvbPan5iu7yZiXJuShGlnOGbw0noy7UN6aJeGjjAShXJgl4
                    GejfAdlvVRJmgDl9yjT0/icTAAwFJlfzOcmoWyJMkUUGe6J8gIACJTEObxyDov5OWieAHimZ+SKBI
                    lJYqYR15hp5ejIZvrxs1P5YjErlMNN4Yh4TM/0tAyOMBeAr2+WRQElWW2ZaJHtrRzt7VnW5mj5v9n
                    fHn5T/T3IevtV8Sbsz55BjJ5Z32zsrC+9FgD2JFqbHbO+lVUAtG0GQOXhrE/vIADyBQC03pzzHoZs
                    XpLE4gwnC4vs7GxzAZ9rLivoN/ufgm/Kv4Y595nL7vtWO6YXP4EjSRUzZUXlpqemS0TMzAwOl89k/
                    fcQ/+PAOWnNycMsnJ/AF/GF6FVR6JQJhIlou4U8gViQLmQKhH/V4X8YNicHGX6daxRodV8AfYU5UL
                    hJB8hvPQBDIwMkbj96An3rWxAxCsi+vGitka9zjzJ6/uf6Hwtcim7hTEEiU+b2DI9kciWiLBmj34R
                    swQISkAd0oAo0gS4wAixgDRyAM3AD3iAAhIBIEAOWAy5IAmlABLJBPtgACkEx2AF2g2pwANSBetAE
                    ToI2cAZcBFfADXALDIBHQAqGwUswAd6BaQiC8BAVokGqkBakD5lC1hAbWgh5Q0FQOBQDxUOJkBCSQ
                    PnQJqgYKoOqoUNQPfQjdBq6CF2D+qAH0CA0Bv0BfYQRmALTYQ3YALaA2bA7HAhHwsvgRHgVnAcXwN
                    vhSrgWPg63whfhG/AALIVfwpMIQMgIA9FGWAgb8URCkFgkAREha5EipAKpRZqQDqQbuY1IkXHkAwa
                    HoWGYGBbGGeOHWYzhYlZh1mJKMNWYY5hWTBfmNmYQM4H5gqVi1bGmWCesP3YJNhGbjS3EVmCPYFuw
                    l7ED2GHsOxwOx8AZ4hxwfrgYXDJuNa4Etw/XjLuA68MN4SbxeLwq3hTvgg/Bc/BifCG+Cn8cfx7fj
                    x/GvyeQCVoEa4IPIZYgJGwkVBAaCOcI/YQRwjRRgahPdCKGEHnEXGIpsY7YQbxJHCZOkxRJhiQXUi
                    QpmbSBVElqIl0mPSa9IZPJOmRHchhZQF5PriSfIF8lD5I/UJQoJhRPShxFQtlOOUq5QHlAeUOlUg2
                    obtRYqpi6nVpPvUR9Sn0vR5Mzl/OX48mtk6uRa5Xrl3slT5TXl3eXXy6fJ18hf0r+pvy4AlHBQMFT
                    gaOwVqFG4bTCPYVJRZqilWKIYppiiWKD4jXFUSW8koGStxJPqUDpsNIlpSEaQtOledK4tE20Otpl2
                    jAdRzek+9OT6cX0H+i99AllJWVb5SjlHOUa5bPKUgbCMGD4M1IZpYyTjLuMj/M05rnP48/bNq9pXv
                    +8KZX5Km4qfJUilWaVAZWPqkxVb9UU1Z2qbapP1DBqJmphatlq+9Uuq43Pp893ns+dXzT/5PyH6rC
                    6iXq4+mr1w+o96pMamhq+GhkaVRqXNMY1GZpumsma5ZrnNMe0aFoLtQRa5VrntV4wlZnuzFRmJbOL
                    OaGtru2nLdE+pN2rPa1jqLNYZ6NOs84TXZIuWzdBt1y3U3dCT0svWC9fr1HvoT5Rn62fpL9Hv1t/y
                    sDQINpgi0GbwaihiqG/YZ5ho+FjI6qRq9Eqo1qjO8Y4Y7ZxivE+41smsImdSZJJjclNU9jU3lRgus
                    +0zwxr5mgmNKs1u8eisNxZWaxG1qA5wzzIfKN5m/krCz2LWIudFt0WXyztLFMt6ywfWSlZBVhttOq
                    w+sPaxJprXWN9x4Zq42Ozzqbd5rWtqS3fdr/tfTuaXbDdFrtOu8/2DvYi+yb7MQc9h3iHvQ732HR2
                    KLuEfdUR6+jhuM7xjOMHJ3snsdNJp9+dWc4pzg3OowsMF/AX1C0YctFx4bgccpEuZC6MX3hwodRV2
                    5XjWuv6zE3Xjed2xG3E3dg92f24+ysPSw+RR4vHlKeT5xrPC16Il69XkVevt5L3Yu9q76c+Oj6JPo
                    0+E752vqt9L/hh/QL9dvrd89fw5/rX+08EOASsCegKpARGBFYHPgsyCRIFdQTDwQHBu4IfL9JfJFz
                    UFgJC/EN2hTwJNQxdFfpzGC4sNKwm7Hm4VXh+eHcELWJFREPEu0iPyNLIR4uNFksWd0bJR8VF1UdN
                    RXtFl0VLl1gsWbPkRoxajCCmPRYfGxV7JHZyqffS3UuH4+ziCuPuLjNclrPs2nK15anLz66QX8FZc
                    SoeGx8d3xD/iRPCqeVMrvRfuXflBNeTu4f7kufGK+eN8V34ZfyRBJeEsoTRRJfEXYljSa5JFUnjAk
                    9BteB1sl/ygeSplJCUoykzqdGpzWmEtPi000IlYYqwK10zPSe9L8M0ozBDuspp1e5VE6JA0ZFMKHN
                    ZZruYjv5M9UiMJJslg1kLs2qy3mdHZZ/KUcwR5vTkmuRuyx3J88n7fjVmNXd1Z752/ob8wTXuaw6t
                    hdauXNu5Tnddwbrh9b7rj20gbUjZ8MtGy41lG99uit7UUaBRsL5gaLPv5sZCuUJR4b0tzlsObMVsF
                    Wzt3WazrWrblyJe0fViy+KK4k8l3JLr31l9V/ndzPaE7b2l9qX7d+B2CHfc3em681iZYlle2dCu4F
                    2t5czyovK3u1fsvlZhW3FgD2mPZI+0MqiyvUqvakfVp+qk6oEaj5rmvep7t+2d2sfb17/fbX/TAY0
                    DxQc+HhQcvH/I91BrrUFtxWHc4azDz+ui6rq/Z39ff0TtSPGRz0eFR6XHwo911TvU1zeoN5Q2wo2S
                    xrHjccdv/eD1Q3sTq+lQM6O5+AQ4ITnx4sf4H++eDDzZeYp9qukn/Z/2ttBailqh1tzWibakNml7T
                    Hvf6YDTnR3OHS0/m/989Iz2mZqzymdLz5HOFZybOZ93fvJCxoXxi4kXhzpXdD66tOTSna6wrt7LgZ
                    evXvG5cqnbvfv8VZerZ645XTt9nX297Yb9jdYeu56WX+x+aem172296XCz/ZbjrY6+BX3n+l37L97
                    2un3ljv+dGwOLBvruLr57/17cPel93v3RB6kPXj/Mejj9aP1j7OOiJwpPKp6qP6391fjXZqm99Oyg
                    12DPs4hnj4a4Qy//lfmvT8MFz6nPK0a0RupHrUfPjPmM3Xqx9MXwy4yX0+OFvyn+tveV0auffnf7v
                    WdiycTwa9HrmT9K3qi+OfrW9m3nZOjk03dp76anit6rvj/2gf2h+2P0x5Hp7E/4T5WfjT93fAn88n
                    gmbWbm3/eE8/syOll+AAAvnElEQVR4Ae2dB7wkRbn2F8kZlHDBVRe4SM4ZREAUUFCQq8gnOccrQUE
                    R+OAaQFcBRSVIWtICwgcXkJxzFCQHCbtLBiVHYeH7P8sMO+ec7p6eOR2qu5/6/d7TM1XVVW/9q08/
                    U9Vd3VOMcDCBmhP46KOPpqKJc2P/gc2DzYnNjM3U2nZ+Hhw3A3mmiLBPRcR9SNzbHfZWx2fFd35/g
                    +8vYi8N2r48xRRTfEScgwmUQkAHu4MJVJYAJ/xZcH5BbH5sXqx94m9vJQJzYFU51ifi6z+xtlhIOJ
                    7HnsTGtbZPIhxv8tnBBDInUJV/lMwb7gKrQ4ATv36968Tftv/s+DxXdVqSqacSDgnFYHtMcR5tZMq
                    6UYVZFBrV3WE3lpP/lHi4CLYstkzLFmKrX/0O6QlomupB7D7s/vYWodCIw8EEEglYFBLxODEvAgjA
                    NJS9OCYBaNuSfJ4ec8iHwL8otlMo7ub73xGL9/OpzqVWkYBFoYq9VkGfEQFd6F0TWwNbBVsMmxpzK
                    JfAu1T/N+zWlt2CSDxTrkuuvUwCFoUy6de4bkRAF3glAGu2tguzdagGgadx8xOR4PNdCIXEw6EBBC
                    wKDejkIprYEoG1qKstBF8sol7XUQgBTS/dgl2JXYHdgUjoLimHGhKwKNSwU4tqEkKgawDfatnybH0
                    8FQW/3Hpeo/prMAnElQjEo+W649qzJOB/4ixp1rwsRECLwL6MbYhJDEZhDiYwAQTtUYREQrfLOlSU
                    gEWhoh1XlNsIwazUtR4mIfg6NhvmYAJxBDStdCN2Lva/CIQEw6FCBCwKFeqsolxtjQgkAFti38SmL
                    apu11M7AnfSovOwcxGIh2vXuho2yKJQw07tt0mIgdYLSAi+j+n5QA4mkCUBiYJGEOchEBILhwAJWB
                    QC7JQiXUII9LygzbCtMK0dcDCBIgiMp5LTsFMQCF+oLoJ4yjosCilB1SkbQqBFYxtj22Bfwz6FOZh
                    AWQR0u+vJ2FkIxKtlOeF6PyZgUWjQkYAY6OFxO2K7YBohOJhASAS0QO58TAJxOQLhtRAl9I5FoQTo
                    RVfZulbwA+rdFPNF46I7wPX1Q+A5djodG4M4PNBPAd6nPwIWhf64Bb8XQqA1BZoikhisFrzDdtAE4
                    glcS9KR2AUePcRDyirFopAVyUDKQQz0FrFdsd2xkYG4ZTdMIAsC4ynkKOx4xOHlLAp0GUMJWBSGMq
                    lkDGKgRWUaFeyJzV7JRthpE0hH4B2y6c6lIxEHvS/CIUMCFoUMYZZRFGIwB/XuhWlkMEsZPrhOEyi
                    RgJ7B1J5a0juyHYZJwKIwTIBl7Y4Y6P0EP8J0J9GMZfnhek0gEAKP48cvsVMZPXwQiE+VdMOiULFu
                    Qwz0noL9sB2w6Srmvt01gbwJjKOCQ7CTEYd/511ZHcu3KFSkVxEDXUDeB/shNkNF3LabJlAWAT2I7
                    1fYiYjDe2U5UcV6LQqB9xpioFtLteDsIEyLzxxMwATSE3iGrL/GjkMctDjOoQsBi0IXQGUmIwjfpn
                    792vFbzMrsCNddBwJaDDcaO9ojh+TutCgk8yklFTFYhYp/g3nRWSk94EprTOBJ2vZjhOHsGrdxWE2
                    zKAwLX7Y7IwZabHY49t1sS3ZpJmACgwjczPe9EYfbBsU3/qufjhnAIaDrBphuL30IsyAE0Cd2ofYE
                    VqWFt/B/Nxb7Qu1b20MDPVLoAVYeWTkgv0S5R2OL51G+yzQBE+hKQBegj8AOZeTwRtfcNc9gUSipg
                    xEDrUTWha+tMfcDEBxMoGQCL1L/gZierdTY1dE+GRV8FCIGYr49pruKPl1w9a7OBEygOwFdb9gBYX
                    iwe9b65bAoFNinCMJCVHcSpruLHEzABMIloNXQh2KHIA6NWhltUSjgoGyNDvbQAYZNX0CVrsIETCA
                    bAhotaNSg0UMjgkUh525GEOajCo0O1si5KhdvAiaQD4GPKFbvcdgPcaj9hWjfkprPQTSpVARhJz7c
                    i1kQcuTsok0gZwL68bwb9iD/09/Mua7Si/dIIYcu4MDRIrQTsHVyKN5FmoAJlEtA747elVHD6+W6k
                    U/tFoWMuSIIm1HkHzG9Cc3BBEygngSeoFmbIgx31K15nj7KqEcRgxkwjQ70mkALQkZcXYwJBEpgfv
                    y6if/5fbBa/biuVWPKOng4KBahbj1ga7GyfHC9JmACpRG4nJq3ZNTwQmkeZFixRwrDhIkgbEkRGkJ
                    aEIbJ0rubQEUJ6NrhPZwL1q2o/wPctigMwJH+CweApotOZI+TsRnT7+mcJmACNSSgd6ZfwjnhN9jU
                    VW6fp4/66D06fVF2+wvm0UEf/LyLCdScwK20b6OqTid5pNDj0YkgbMIuni7qkZuzm0CDCKxMW+/gX
                    LF0FdtsUUjZa3TwFNj/kP0sbIaUuzmbCZhAMwl8jmbfyDlDr9StVPD0UYruomN1zeAUbOMU2Z3FBE
                    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" y="0" x="0" height="50" width="50" id="image0"></image>
                    </svg>
                    <svg viewBox="0 0 48 48" height="36" width="36" y="0px" x="0px" xmlns="http://www.w3.org/2000/svg" class="logo">
                    <path d="M32 10A14 14 0 1 0 32 38A14 14 0 1 0 32 10Z" fill="#ff9800"></path><path d="M16 10A14 14 0 1 0 16 38A14 14 0 1 0 16 10Z" fill="#d50000"></path><path d="M18,24c0,4.755,2.376,8.95,6,11.48c3.624-2.53,6-6.725,6-11.48s-2.376-8.95-6-11.48 C20.376,15.05,18,19.245,18,24z" fill="#ff3d00"></path>
                    </svg>
                    <p class="heading_8264">MASTERCARD</p>
                    <svg xml:space="preserve" viewBox="0 0 50 50" height="30px" width="30px" y="0px" x="0px" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" id="Layer_1" class="chip" version="1.1">  <image href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAMAAAAp4XiDAAAABGdBTUEAALGPC/xhBQAAACBjSFJN
                    AAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAB6VBMVEUAAACNcTiVeUKVeUOY
                    fEaafEeUeUSYfEWZfEaykleyklaXe0SWekSZZjOYfEWYe0WXfUWXe0WcgEicfkiXe0SVekSXekSW
                    ekKYe0a9nF67m12ZfUWUeEaXfESVekOdgEmVeUWWekSniU+VeUKVeUOrjFKYfEWliE6WeESZe0GS
                    e0WYfES7ml2Xe0WXeESUeEOWfEWcf0eWfESXe0SXfEWYekSVeUKXfEWxklawkVaZfEWWekOUekOW
                    ekSYfESZe0eXekWYfEWZe0WZe0eVeUSWeETAnmDCoWLJpmbxy4P1zoXwyoLIpWbjvXjivnjgu3bf
                    u3beunWvkFWxkle/nmDivXiWekTnwXvkwHrCoWOuj1SXe0TEo2TDo2PlwHratnKZfEbQrWvPrWua
                    fUfbt3PJp2agg0v0zYX0zYSfgkvKp2frxX7mwHrlv3rsxn/yzIPgvHfduXWXe0XuyIDzzISsjVO1
                    lVm0lFitjVPzzIPqxX7duna0lVncuHTLqGjvyIHeuXXxyYGZfUayk1iyk1e2lln1zYTEomO2llrb
                    tnOafkjFpGSbfkfZtXLhvHfkv3nqxH3mwXujhU3KqWizlFilh06khk2fgkqsjlPHpWXJp2erjVOh
                    g0yWe0SliE+XekShhEvAn2D///+gx8TWAAAARnRSTlMACVCTtsRl7Pv7+vxkBab7pZv5+ZlL/UnU
                    /f3SJCVe+Fx39naA9/75XSMh0/3SSkia+pil/KRj7Pr662JPkrbP7OLQ0JFOijI1MwAAAAFiS0dE
                    orDd34wAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfnAg0IDx2lsiuJAAACLElEQVRIx2Ng
                    GAXkAUYmZhZWPICFmYkRVQcbOwenmzse4MbFzc6DpIGXj8PD04sA8PbhF+CFaxEU8iWkAQT8hEVg
                    OkTF/InR4eUVICYO1SIhCRMLDAoKDvFDVhUaEhwUFAjjSUlDdMiEhcOEItzdI6OiYxA6YqODIt3d
                    I2DcuDBZsBY5eVTr4xMSYcyk5BRUOXkFsBZFJTQnp6alQxgZmVloUkrKYC0qqmji2WE5EEZuWB6a
                    lKoKdi35YQUQRkFYPpFaCouKIYzi6EDitJSUlsGY5RWVRGjJLyxNy4ZxqtIqqvOxaVELQwZFZdkI
                    JVU1RSiSalAt6rUwUBdWG1CP6pT6gNqwOrgCdQyHNYR5YQFhDXj8MiK1IAeyN6aORiyBjByVTc0F
                    qBoKWpqwRCVSgilOaY2OaUPw29qjOzqLvTAchpos47u6EZyYnngUSRwpuTe6D+6qaFQdOPNLRzOM
                    1dzhRZyW+CZouHk3dWLXglFcFIflQhj9YWjJGlZcaKAVSvjyPrRQ0oQVKDAQHlYFYUwIm4gqExGm
                    BSkutaVQJeomwViTJqPK6OhCy2Q9sQBk8cY0DxjTJw0lAQWK6cOKfgNhpKK7ZMpUeF3jPa28BCET
                    amiEqJKM+X1gxvWXpoUjVIVPnwErw71nmpgiqiQGBjNzbgs3j1nus+fMndc+Cwm0T52/oNR9lsdC
                    S24ra7Tq1cbWjpXV3sHRCb1idXZ0sGdltXNxRateRwHRAACYHutzk/2I5QAAACV0RVh0ZGF0ZTpj
                    cmVhdGUAMjAyMy0wMi0xM1QwODoxNToyOSswMDowMEUnN7UAAAAldEVYdGRhdGU6bW9kaWZ5ADIw
                    MjMtMDItMTNUMDg6MTU6MjkrMDA6MDA0eo8JAAAAKHRFWHRkYXRlOnRpbWVzdGFtcAAyMDIzLTAy
                    LTEzVDA4OjE1OjI5KzAwOjAwY2+u1gAAAABJRU5ErkJggg==" y="0" x="0" height="50" width="50" id="image0"></image>
                    </svg>
                    <svg xml:space="preserve" viewBox="0 0 50 50" height="20px" width="20px" y="0" x="0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" id="Layer_1" class="contactless" version="1.1">  <image href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAQAAAC0NkA6AAAABGdBTUEAALGPC/xhBQAAACBjSFJN
                    AAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QA/4ePzL8AAAAJcEhZ
                    cwAACxMAAAsTAQCanBgAAAAHdElNRQfnAg0IEzgIwaKTAAADDklEQVRYw+1XS0iUURQ+f5qPyjQf
                    lGRFEEFK76koKGxRbWyVVLSOgsCgwjZBJJYuKogSIoOonUK4q3U0WVBWFPZYiIE6kuArG3VGzK/F
                    fPeMM/MLt99/NuHdfPd888/57jn3nvsQWWj/VcMlvMMd5KRTogqx9iCdIjUUmcGR9ImUYowyP3xN
                    GQJoRLVaZ2DaZf8kyjEJALhI28ELioyiwC+Rc3QZwRYyO/DH51hQgWm6DMIh10KmD4u9O16K49it
                    VoPOAmcGAWWOepXIRScAoJZ2Frro8oN+EyTT6lWkkg6msZfMSR35QTJmjU0g15tIGSJ08ZZMJkJk
                    HpNZgSkyXosS13TkJpZ62mPIJvOSzC1bp8vRhhCakEk7G9/o4gmZdbpsTcKu0m63FbnBP9Qrc15z
                    bkbemfgNDtEOI8NO5L5O9VYyRYgmJayZ9nPaxZrSjW4+F6Uw9yQqIiIZwhp2huQTf6OIvCZyGM6g
                    DJBZbyXifJXr7FZjGXsdxADxI7HUJFB6iWvsIhFpkoiIiGTJfjJfiCuJg2ZEspq9EHGVpYgzKqwJ
                    qSAOEwuJQ/pxPvE3cYltJCLdxBLiSKKIE5HxJKcTRNeadxfhDiuYw44zVs1dxKwRk/uCxIiQkxKB
                    sSctRVAge9g1E15EHE6yRUaJecRxcWlukdRIbGFOSZCMWQA/iWauIP3slREHXPyliqBcrrD71Amz
                    Z+rD1Mt2Yr8TZc/UR4/YtFnbijnHi3UrN9vKQ9rPaJf867ZiaqDB+czeKYmd3pNa6fuI75MiC0uX
                    XSR5aEMf7s7a6r/PudVXkjFb/SsrCRfROk0Fx6+H1i9kkTGn/E1vEmt1m089fh+RKdQ5O+xNJPUi
                    cUIjO0Dm7HwvErEr0YxeibL1StSh37STafE4I7zcBdRq1DiOkdmlTJVnkQTBTS7X1FYyvfO4piaI
                    nKbDCDaT2anLudYXCRFsQBgAcIF2/Okwgvz5+Z4tsw118dzruvIvjhTB+HOuWy8UvovEH6beitBK
                    xDyxm9MmISKCWrzB7bSlaqGlsf0FC0gMjzTg6GgAAAAldEVYdGRhdGU6Y3JlYXRlADIwMjMtMDIt
                    MTNUMDg6MTk6NTYrMDA6MDCjlq7LAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDIzLTAyLTEzVDA4OjE5
                    OjU2KzAwOjAw0ssWdwAAACh0RVh0ZGF0ZTp0aW1lc3RhbXAAMjAyMy0wMi0xM1QwODoxOTo1Nisw
                    MDowMIXeN6gAAAAASUVORK5CYII=" y="0" x="0" height="50" width="50" id="image0"></image>
                    </svg>
                    <p class="number">{card_number}</p>
                    <p class="valid_thru">VALID THRU</p>
                    <p class="date_8264">{card_expiration}</p>
                    <p class="name">{card_owner}</p>
                </div>
                <div class="flip-card-back">
                    <div class="strip"></div>
                    <div class="mstrip"></div>
                    <div class="sstrip">
                    <p class="code">***</p>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True
)
    
st.divider()
    
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label=card_settings.name[0], value=str(card_settings.isEnable[0]), help=card_settings.description[0])

with col2:
    st.metric(label=card_settings.name[1], value=str(card_settings.isEnable[1]), help=card_settings.description[1])

with col3:
    st.metric(label=card_settings.name[2], value=str(card_settings.isEnable[2]), help=card_settings.description[2])

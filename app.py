from typing import Dict

from flask import Flask
from flask_jsonrpc import JSONRPC

app = Flask(__name__)

api = JSONRPC(app, "/api/v1/", enable_web_browsable_api=True)

USER_EMAIL = "jantje@beton.nl"
USER_TOKEN = "09KfFta3MmtBFiTz55lzqG8WcOR_IZPb8s1F4LHpZ0b1iuw"


@api.method("validate_ticket")
def validate_ticket(email: str, token: str, qr_data: dict) -> dict:

    valid_ticket_tokens = [
        "pu_ztHGAw-1sBNcXWJzKV7m3Gg6LPd4_94a8RBhXDpakSfk",
        "4D4Ct4Ydxj_x5qz-Q2B_4hur5T7iUF5z8fPTTv6bo7vjxaY",
        "Dk5ZGzRm_fz4XCZPjKFVbR1yRQX-Ue4s1PZ_5HOLY6qnCHo",
        "yrT5HNgXIM7x4snjtYLdNpsYUqvph7X--2uQpjGhybl9N78",
    ]

    if email != USER_EMAIL or token != USER_TOKEN:
        return {
            "code": "UNAUTHORIZED",
            "message": f"user {email} is not authorized to validate tickets"
        }

    token = qr_data.get("token", None)

    if token is None or token not in valid_ticket_tokens:
        return {
            "code": "INVALID",
            "message": "Ticket could not be validated"
        }

    else:
        return {
            "code": "OK",
            "message": "Ticket Validation Succeeded"
        }


if __name__ == "__main__":
    app.run("0.0.0.0", port=5050)
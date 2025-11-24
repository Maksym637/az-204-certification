import json

from enum import Enum

from http import HTTPStatus

import azure.functions as func

from deep_translator import GoogleTranslator

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


class SupportedLanguages(str, Enum):
    ENGLISH = "en"
    GERMAN = "de"
    FRENCH = "fr"
    SPANISH = "es"
    PORTUGUESE = "pt"

    @classmethod
    def list(cls) -> list[str]:
        return [language.value for language in cls]


@app.route(route="translator_trigger", methods=["POST"])
def translator_trigger(req: func.HttpRequest) -> func.HttpResponse:
    request_body = req.get_json()

    text_to_translate = request_body.get("text", None)
    source_language = request_body.get("source", None)
    target_language = request_body.get("target", None)

    if not text_to_translate:
        return func.HttpResponse(
            body="Missing the 'text' field in request body",
            status_code=HTTPStatus.BAD_REQUEST,
        )

    if (
        source_language not in SupportedLanguages.list()
        or target_language not in SupportedLanguages.list()
    ):
        return func.HttpResponse(
            body="The provided language is not supported",
            status_code=HTTPStatus.BAD_REQUEST,
        )

    try:

        translated_text = GoogleTranslator(
            source=source_language, target=target_language
        ).translate(text=text_to_translate)

    except Exception as error:
        return func.HttpResponse(
            body=f"Translation failed: {str(error)}",
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        )

    return func.HttpResponse(
        body=json.dumps({"translated_text": translated_text}, ensure_ascii=False),
        mimetype="application/json",
        status_code=HTTPStatus.OK,
    )

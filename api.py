import base64
import json
from http import HTTPStatus

from tornado.web import RequestHandler

from models import items


class LookItems(RequestHandler):

    async def get(self):
        self.write({'items': items})


class TotalDuplicate(RequestHandler):
    async def get(self):
        try:
            count_duplicates = 0
            count_request = 0
            for value in items.values():
                count_duplicates += (len(value) - 1)
                count_request += len(value)

            if not count_duplicates:
                self.write("There are no duplicates")
            else:
                duplicates_rate = float(
                    "{:.2f}".format(
                        (count_duplicates/count_request)
                    )
                ) * 100
                self.write(f"Total duplicates: {duplicates_rate}%")

        except Exception:
            self.send_error(status_code=HTTPStatus.NOT_FOUND)


class ItemCRUD(RequestHandler):

    async def get(self, key_id):
        try:
            if key_id in items:
                self.write(
                    {
                        'body': items[key_id][0],
                        'duplicates': len(items[key_id])-1
                    }
                )
            else:
                self.write({})
        except Exception:
            self.send_error(status_code=HTTPStatus.BAD_REQUEST)

    async def post(self, _):
        try:
            params = json.loads(self.request.body.decode())
            key_param, value_param = '', ''
            if params:
                for key, value in params.items():
                    key_param += key
                    value_param += value if not isinstance(
                        value, list
                    ) else ''.join(value)

                result = base64.b64encode(
                    (
                        key_param + value_param
                    ).encode('ascii')
                ).decode('ascii')

                items.setdefault(result, []).append(params)
                self.write({'generated_key': result})
        except Exception:
            self.send_error(status_code=HTTPStatus.BAD_REQUEST)

    async def put(self, key_id):
        try:
            if key_id in items:

                params = json.loads(self.request.body.decode())
                new_item = items[key_id][0]
                del items[key_id]

                for key_param in params:
                    if key_param in new_item:
                        new_item[key_param] = params[key_param]

                key_param, value_param = '', ''

                for key in new_item:
                    key_param += key
                    value_param += new_item[key]

                result = base64.b64encode(
                    (
                        key_param + value_param
                    ).encode('ascii')
                ).decode('ascii')

                items.setdefault(result, []).append(params)
                self.write({'generated_key': result})

            else:
                self.send_error(
                    status_code=HTTPStatus.NOT_FOUND,
                    message="Update Does Not Exist"
                )

        except Exception:
            self.send_error(status_code=HTTPStatus.BAD_REQUEST)

    async def delete(self, key_id):
        try:
            if key_id in items:
                del items[key_id]
            else:
                self.send_error(
                    status_code=HTTPStatus.NOT_FOUND,
                    message="Delete Does Not Exist"
                )
        except Exception:
            self.send_error(status_code=HTTPStatus.BAD_REQUEST)

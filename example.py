from pysignald_async import SignaldAPI
import asyncio
from pysignald_async.api import JsonAddressv1, JsonMessageEnvelopev1

class EchoBot(SignaldAPI):
    def handle_envelope(self, envelope: JsonMessageEnvelopev1):
        message = envelope.dataMessage
        source = envelope.source.number
        # envelopes contain typing notifications, receipts, so
        # let's check if it's actually a messages
        if message is not None and source is not None:
            # signald can handle multiple accounts
            username = envelope.username
            asyncio.create_task(
                self.signald.send(
                    username=user.legacy_id,
                    recipientAddress=JsonAddressv1(
                        number=legacy_buddy_id),
                    messageBody=message.body,
                )
            )

async def main():
    loop = asyncio.get_running_loop()
    _, signald = await loop.create_unix_connection(
        SignaldAPI, path=SIGNALD_SOCKET_PATH)
    # Username is a phone number that has either been registered or linked in signald
    await signald.subscribe(username="+XXXXXX")

SIGNALD_SOCKET_PATH = "/var/run/signald/signald.sock"

asyncio.run(main())
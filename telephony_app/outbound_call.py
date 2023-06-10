import os
from dotenv import load_dotenv

load_dotenv()

from vocode.streaming.telephony.conversation.outbound_call import OutboundCall
from vocode.streaming.telephony.config_manager.redis_config_manager import (
    RedisConfigManager,
)

from vocode.streaming.models.synthesizer import GoogleSynthesizerConfig


from speller_agent import SpellerAgentConfig

BASE_URL = os.environ["BASE_URL"]

config_manager = RedisConfigManager()

outbound_call = OutboundCall(
    base_url=BASE_URL,
    synthesizer_config=GoogleSynthesizerConfig.from_telephone_output_device(
        api_key=os.environ["GOOGLE_SPEECH_KEY"]
    ),
    to_phone="+18555831599",
    from_phone="+16305495618",
    config_manager=config_manager,
    agent_config=SpellerAgentConfig(generate_responses=False),
)

input("Press enter to start call...")
outbound_call.start()

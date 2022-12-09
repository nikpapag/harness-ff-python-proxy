import time
import os

from featureflags.evaluations.auth_target import Target
from featureflags.client import CfClient
from featureflags.util import log
from featureflags.config import with_base_url, with_analytics_enabled, with_stream_enabled, Config
from featureflags.config import with_events_url


def main():
    api_key = os.getenv('HARNESS_API_KEY')
    relay_proxy_url = os.getenv('HARNESS_RELAY_PROXY')
    flag_name = os.getenv('HARNESS_FF_NAME')
    target_identifier = os.getenv('HARNESS_TARGET_IDENTIFIER')
    target_name = os.getenv('HARNESS_TARGET_NAME')
    log.debug("Starting example")

    client = CfClient(api_key,
                      with_base_url(relay_proxy_url),
                      with_events_url(relay_proxy_url))
    target = Target(identifier=target_identifier, name=target_name,attributes={"location": "emea"})

    while True:
        result = client.bool_variation(flag_name, target, False)
        log.debug("Result %s", result)
        time.sleep(10)

if __name__ == "__main__":
    main()

# Copyright 2024 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import sys

from solution.consumer_sol import mqConsumer  # pylint: disable=import-error

def main(tickers,sectors,queueName) -> None:
    
    # Implement Logic to Create Binding Key from the ticker and sector variable -  Step 2
    #
    #                       WRITE CODE HERE!!!
    #

    binding_keys = []
    for ticker in tickers:
        for sector in sectors:
            binding_keys.append("*."+ticker+"."+sector)
    print(binding_keys)

    consumer = mqConsumer(binding_keys=binding_keys,exchange_name="Tech Lab Topic Exchange",queue_name=queueName)    
    consumer.startConsuming()
    


if __name__ == "__main__":

    # Implement Logic to read the sector and queueName string from the command line and save them - Step 1
    #
    #                       WRITE CODE HERE!!!
    #
    num_tickers = sys.argv[1]
    num_sectors = sys.argv[2]
    tickers = []
    sectors = []
    for i in range(3,3+int(num_tickers)):
        tickers.append(sys.argv[i])
        print(sys.argv[i])
    for i in range(3+int(num_tickers), 3+int(num_tickers)+int(num_sectors)):
        sectors.append(sys.argv[i])
        print(sys.argv[i])
    queue = sys.argv[int(num_tickers)+int(num_sectors)-1]
    sys.exit(main(tickers, sectors, queue))

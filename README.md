# DoH-Exfiltration-Detection
As DNS-over-HTTPS gets closer to being a standard, viewing it as a discrete exfiltration tool might be pretty appealing for attackers.
Because of the imposed risk of abuse of data exfiltration and potentially command & control, I feel like it might be a bit interesting to at least look at.

Application traffic analyzed in this project thus far include
* Chrome's built-in DoH
* Firefox's built-in DoH
* [Stamparm's Python-DoH](https://github.com/stamparm/python-doh)

DoH provider traffic analyzed in this project thus far include
* Cloudflare's DoH server

Tentative results demonstrate that the default DoH options used in browsers can be picked out from typical browsing traffic with decent certainty.
As for detecting exfiltration, the python client I useed to generate the data isn't perfect and gives quite a few red flags
that stand out compared to the Browsers' DoH queries.
So while not explicitly detecting exfiltration right now, it can spot that Python client from a mile away.

Future developments later down the line should include tests of other exfiltration scripts,
modifications to the python scripts, and fixing the horrible feature engineering scripts.

# Acknowledgements
* [Zachary Mueller - Fast.AI Lessons](https://github.com/muellerzr/Practical-Deep-Learning-for-Coders-2.0)
* [Starparm - Python DoH client](https://github.com/stamparm/python-doh)

# License
This project and its contents are open-source under the MIT License.

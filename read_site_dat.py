import pickle
import os
from config import Config

with open(os.path.join(Config().get_inner_config_path(),
                                   "sites.dat"),
                      "rb") as f:
    data = pickle.load(f)
    indexer = data.get("indexer")
    for item in indexer:
        if item['id'] == 'chdbits':
            item['domain'] = 'https://ptchdbits.co/'

    conf = data.get("conf")
    conf['ptchdbits.co'] = conf["chdbits.co"]

    # print(conf['ptchdbits.co'])

    print(str(data))

    with open("newsites.dat", 'wb') as file:
        pickle.dump(data, file)
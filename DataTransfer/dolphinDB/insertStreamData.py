from utils import config
import dolphindb as ddb


sessionTemp = ddb.session()
sessionTemp.connect(config.Configuration.dolphindb_ip, config.Configuration.dolphindb_port,
                    config.Configuration.dolphindb_user, config.Configuration.dolphindb_password,
                    '', False, [], -1, False)
sessionTemp.run("data = select 'zhugeliang','book_name_001','strategy_001','30.3' from test_stream;tableInsert("
                "'test_stream',data)")
from MsgID.csfile import genCSfile
from MsgID.gofile import genGolangfile
from MsgID.proto import loadProto
import subprocess

from const import cs_msg_path, go_msg_path, proto_path

protocCsCmd = 'protoc --proto_path=./Proto/src  --csharp_out=' + cs_msg_path + ' ' + proto_path + '/*.proto'
protocGoCmd = 'protoc --proto_path=./Proto/src      --go_out=' + go_msg_path + ' ' + proto_path + '/*.proto'

print("开始执行命令：" + protocCsCmd)
subprocess.call(protocCsCmd)
print("开始执行命令：" + protocGoCmd)
subprocess.call(protocGoCmd)
print("开始生成管理文件：")
protos = loadProto()
genCSfile(protos)
genGolangfile(protos)
print("finished...")







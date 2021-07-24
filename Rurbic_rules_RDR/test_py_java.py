import jpype
import Data_curation_API
#得到默认的 JVM 路径
jvmpath=jpype.getDefaultJVMPath()
#启动jvm
jpype.startJVM(jvmpath)
#打印
jpype.java.lang.System.out.println("dsfsfsfds")

#关闭jvm
jpype.shutdownJVM()
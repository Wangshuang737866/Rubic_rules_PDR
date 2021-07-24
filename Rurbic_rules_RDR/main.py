import jpype
import os

if __name__ == '__main__':
    """
    基本的开发流程如下：
    ①、使用jpype开启jvm
    ②、加载java类
    ③、调用java方法
    ④、关闭jvm（不是真正意义上的关闭，卸载之前加载的类）
    """
    # ①、使用jpype开启虚拟机（在开启jvm之前要加载类路径）

    # 加载刚才打包的jar文件
    jarpath = os.path.join(os.path.abspath("."), "F:/work/Data-curation-API/target/TextAPI-0.0.1-SNAPSHOT-shaded.jar")

    # 获取jvm.dll 的文件路径
    jvmPath = jpype.getDefaultJVMPath()


    # 开启jvm
    jpype.startJVM(jvmPath,"-ea", "-Djava.class.path=%s" % (jarpath))
    jpype.java.lang.System.out.println('hello')
    # ②、加载java类（参数是java的长类名）
    javaClass = jpype.JClass("unsw.curation.api.Main")

    # 实例化java对象
    # javaInstance = javaClass()

    # ③、调用java方法，由于我写的是静态方法，直接使用类名就可以调用方法

    print(javaClass.extractEntityFile_method("tweets.txt"))

    # ④、关闭jvm
    jpype.shutdownJVM()
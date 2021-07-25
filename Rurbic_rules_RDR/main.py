import jpype
import os

if __name__ == '__main__':
    # """
    # 基本的开发流程如下：
    # ①、使用jpype开启jvm
    # ②、加载java类
    # ③、调用java方法
    # ④、关闭jvm（不是真正意义上的关闭，卸载之前加载的类）
    # """
    # ①、使用jpype开启虚拟机（在开启jvm之前要加载类路径）

    # 加载刚才打包的jar文件
    jarpath = os.path.join(os.path.abspath("."), '/Users/iti/Desktop/ITIC/Data_curation_API/target/TextAPI-0.0.1-SNAPSHOT.jar')

    # 获取jvm.dll 的文件路径

    # 开启jvm
    jpype.startJVM('/Library/Java/JavaVirtualMachines/jdk1.8.0_301.jdk/Contents/Home/jre/lib/server/libjvm.dylib',
                   "-ea", "-Djava.class.path=%s" % (jarpath))
    # ②、加载java类（参数是java的
    extraction_class = jpype.JClass('unsw.curation.api.Extraction')



    print(extraction_class.extractEntityFile_method("tweets.txt"))

    # ④、关闭jvm
    jpype.shutdownJVM()
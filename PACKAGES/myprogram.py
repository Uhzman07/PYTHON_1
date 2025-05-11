# This is to import from the actual package
from MyMainPackage import some_main_script # This is to import the module from the actual package
from MyMainPackage.SubPackage import mysubscript # This is to import the module from the sub package

# This is used to call the actual function from the created module
some_main_script.report_main()

# This is from the SubPackage
mysubscript.sub_report()
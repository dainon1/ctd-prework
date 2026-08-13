Enter the current year: 2025
Enter the birth year: 1944
You can enter at the casino.


** Process exited - Return Code: 0 **
Traceback (most recent call last):
  File "<exec>", line 3, in <module>
  File "<exec>", line 141, in do_run
  File "main.py", line 5, in <module>
    CurrentYear = int(input("Enter the current year: ")) #Number will represent current year
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<exec>", line 46, in _worker_input
  File "https://www.online-python.com/assets/dist/js/pyodide-worker.js?v=4", line 258, in self._workerRequestInputSync
pyodide.ffi.JsException: SyntaxError: JSON.parse: unexpected character at line 1 column 1 of the JSON data

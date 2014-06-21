"""
#Description
You're a well known web-dev with far too much confidence, you mistakingly agreed to complete too many projects in too little a timeframe. In order to fix this, you devise a program that will automatically write all of the HTML for you!

But first, you'll need to program it.

#Formal Inputs &amp; Outputs

##Input description

On standard console input you should be prompted to enter a paragraph.

##Output description

Once your paragraph has been entered, it should be saved as a valid HTML file and opened in your default brower to display the results

#Sample Inputs &amp; Outputs

##Input

    "Enter your paragraph:"
    "This is my paragraph entry"

##Output
(this is the expected content of the .html file)

    &lt;!DOCTYPE html&gt;
    &lt;html&gt;
        &lt;head&gt;
            &lt;title&gt;&lt;/title&gt;
        &lt;/head&gt;

        &lt;body&gt;
            &lt;p&gt;This is my paragraph entry&lt;/p&gt;
        &lt;/body&gt;
    &lt;/html&gt;

#Bonus

Implement a good looking default CSS style-sheet that also gets automatically generated.
Web browser opener works on linux, can easily modify to work on other platforms. 
"""
import subprocess

def make_html_file(paragraph):
    """
    Makes an html file with a paragraph in the body with the contents of input paragraph.
    Returns filename
    """
    f = open(paragraph.split()[0]+'.html', 'w')
    html_content = """ <!DOCTYPE html>
    <html>
        <head>
            <title></title>
        </head>
        <body>
            <p>%s</p>
        </body>
    </html> """ % (paragraph)
    f.write(html_content)
    f.close()
    return paragraph.split()[0]+'.html'




if __name__ == "__main__":
   filepath = make_html_file( raw_input("Enter your paragraph:"))
   subprocess.call(('xdg-open', filepath))
   #For Mac OSX
   #subprocess.call(('open', filepath)) 
   #For windows
   #os.startfile(filepath)

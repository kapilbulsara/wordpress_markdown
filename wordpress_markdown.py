import xml.etree.ElementTree as ET
import sys
from datetime import datetime
import html2text
import re

xmlFile = sys.argv[1]
outputDir = sys.argv[2]
timezone = 'EST'

tree = ET.parse(xmlFile)
root = tree.getroot()
channel = root.find('channel');
numPosts = 0
numComments = 0
for post in channel.findall('item'):

    namespace_wp = '{http://wordpress.org/export/1.2/}'
    namespace_content = '{http://purl.org/rss/1.0/modules/content/}'
    postType = post.find(namespace_wp + 'post_type').text
    postId = post.find(namespace_wp + 'post_id').text

    if postType == 'post':
        #print (postId)
        postTitle = post.find('title').text
        postName = post.find(namespace_wp + 'post_name').text

        if postName is not None:
            postName = postName.replace('/','_')
        elif postName is None and postTitle is not None :
            postName = postTitle
        else:
            postName = ''
            postTitle = ''
        if postTitle is None and postName is not None: 
            postTitle = postName

        postDateRaw = post.find('pubDate').text
        if postDateRaw is None: 
            postDate = datetime.strptime(post.find(namespace_wp +  'post_date').text, '%Y-%m-%d %H:%M:%S')
        else:
            postDate = datetime.strptime(postDateRaw, '%a, %d %b %Y %H:%M:%S %z')

        postYear = postDate.strftime('%Y')
        postMonth = postDate.strftime('%m')
        postDay = postDate.strftime('%d')
        postHour = postDate.strftime('%H')
        postMinute = postDate.strftime('%M')
        postSecond = postDate.strftime('%S')

        filename = postYear + postMonth + postDay  + '_' + postHour + postMinute + postSecond + '_' + postName
        if len(postTitle) == 0:
            postTitle = filename
        filename =  outputDir + filename  + '.md'

        markdownFile = open(filename, 'w')
        markdownFile.write('# ' + postTitle)
        markdownFile.write('\n')
        markdownFile.write('\n')
        markdownFile.write('Time: ' + postDate.strftime('%a %b %d %H:%M:%S ' + timezone + '  %Y'))
        markdownFile.write('\n')
        markdownFile.write('\n')

        contentHTML = post.find(namespace_content + 'encoded').text
        if contentHTML is not None and len(contentHTML) > 0:
            h = html2text.HTML2Text()
            h.body_width = 0
            contentMarkdown = h.handle(contentHTML)
            markdownFile.write(contentMarkdown)

            print ('saved ' + postName + ' in ' + filename)

        commentStart = False

        for comment in post.findall(namespace_wp + 'comment'):
            if not commentStart:
                commentStart = True
                markdownFile.write('\n')
                markdownFile.write('\n')
                markdownFile.write('## Comments')
                markdownFile.write('\n')
                markdownFile.write('\n')
            #comment date is not consistent with post dates. If needed I shall make it so
            comment_date = comment.find(namespace_wp + 'comment_date').text
            comment_content = comment.find(namespace_wp + 'comment_content').text

            markdownFile.write('Time: ' + comment_date)
            markdownFile.write('\n')
            markdownFile.write('\n')
            
            markdownFile.write(comment_content)
            markdownFile.write('\n')
            markdownFile.write('\n')

            numComments = numComments + 1
            # for my needs I only need date and content 
            # I will add more details on request 


        numPosts = numPosts + 1

print(str(numPosts) + ' wordpress posts exported')
print(str(numComments) + ' wordpress comments exported')

comments = [
    {
        'commentId': 1,
        'commentContent': 'Hai',
        'replies': [
            {
                'commentId': 11,
                'commentContent': 'Hai juga',
                'replies': [
                    {
                        'commentId': 111,
                        'commentContent': 'Haai juga hai jugaa'
                    },
                    {
                        'commentId': 112,
                        'commentContent': 'Haai juga hai jugaa'
                    }
                ]
            },
            {
                'commentId': 12,
                'commentContent': 'Hai juga',
                'replies': [
                    {
                        'commentId': 121,
                        'commentContent': 'Haai juga hai jugaa'
                    }
                ]
            }
        ]
    },
    {
        'commentId': 2,
        'commentContent': 'Halooo'
    }
]

def read_comments(comments):
    com= []
    for comment in comments:
        com.append(comment['commentContent'])
        if 'replies' in comment:
            com+=read_comments(comment['replies'])
    return com


# Membaca semua komentar
print("Terdapat sejumlah: "+str(len(read_comments(comments))) + " Comment")

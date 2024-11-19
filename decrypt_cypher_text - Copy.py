def decrypt_cypher_text(encrypted_text, key):
    encrypted_text = "Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorsh"
    key = 3
    decrypt_cypher_text = list(encrypted_text)#
    decrypted_text = ""
    for x in decrypt_cypher_text:
        y = ord(x)
        decrypted_text = decrypted_text + chr(y-key)
    return decrypted_text
print(decrypt_cypher_text("Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorsh"))
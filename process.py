import plot
import mail
import os

def check_dir(definitions you will use ):
    your_path1 = os.path.expanduser(f"/path")
    your_path2 = os.path.join(your_path1, "plot")
    if os.path.exists(your_path2):
        print("Not processed earthquake couldn't found.")      
        pass
    else:
        plot.raw(definitions you will use)
        sender = 'mail@gmail.com'  
        sender_password = 'password'  
        receivers = ['niyazibedripamukcu@gmail.com']
        subject = f''  
        message = f' '
        
        mail.send(sender, sender_password, receivers, subject, message,  your_path2)

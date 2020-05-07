import subprocess


def check_kubefwd_running(key_words=["redis", "rubbitmq"]):
    """
        Check if the kudefwd is running
    """
    name = "kubefwd"
    p = subprocess.Popen([f"ps aux | grep {name}"], stdout=subprocess.PIPE, shell=True)
    communicate = p.communicate()
    if any(key_word in communicate[0].decode() for key_word in key_words):
        print(
            "*** WARNING ***: Oops,  It seems that the Kubefwd is running, make sure it is not running before building the local environment or run the tests"
        )
        return True

    return False
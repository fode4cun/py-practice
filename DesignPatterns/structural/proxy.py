"""
An object funnels operations to something else.

Proxy is used in places where you want to add functionality to a class without
changing its interface. The main class is called `Real Subject`. A client should
use the proxy or the real subject without any code change, so both must have the
same interface. Logging and controlling access to the real subject are some of
the proxy pattern usages.
"""
from typing import Union


class Subject:
    """
    As mentioned in the document, interfaces of both RealSubject and Proxy should
    be the same, because the client should be able to use RealSubject or Proxy with
    no code change.

    Not all times this interface is necessary. The point is the client should be
    able to use RealSubject or Proxy interchangeably with no change in code.
    """

    def do_the_job(self, user: str) -> None:
        raise NotImplementedError()


class RealSubject(Subject):
    """
    This is the main job doer. External services like payment gateways can be a
    good example.
    """

    def do_the_job(self, user) -> None:
        print(f"I'm doing the job for {user}")


class Proxy(Subject):

    def __init__(self):
        self._real_subject = RealSubject()

    def do_the_job(self, user: str) -> None:
        """
        logging and controlling access are some examples of proxy usages.
        """

        print(f"[log] Doing the job for {user} is requested.")

        if user == "admin":
            self._real_subject.do_the_job(user)
        else:
            print("[log] I can do the job just for `admins`.")


def client(job_doer: Union[RealSubject, Proxy], user: str) -> None:
    job_doer.do_the_job(user)


if __name__ == '__main__':
    proxy = Proxy()
    real_subject = RealSubject()

    client(proxy, 'admin')
    client(proxy, 'anonymous')
    client(real_subject, 'admin')
    client(real_subject, 'anonymous')

using UnityEngine;
using System.Collections;

namespace LeefClient.Demo
{
    public class NetDemo : MonoBehaviour
    {
        void Start()
        {
            InitNet();
            InitManager();
//        ChatView.OpenView("Prefabs/ChatView/ChatView");
        }

        private void InitNet()
        {
            gameObject.AddComponent<NetManager>();
            //NetManager.Instance.SendConnect();
        }

        private void InitManager()
        {
            gameObject.AddComponent<LoginModel>();
            gameObject.AddComponent<ChatModel>();
        }
    }
}

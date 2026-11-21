const channel = new BroadcastChannel('my_channel');
export const broadcastLogout = () => {
  channel.postMessage({ type: 'logout' });
}
export const listenToLogout = (callback: () => void) => {
    channel.onmessage=(event) => {
        if (event?.data?.type === 'logout') {
            callback();
        }
    }
}
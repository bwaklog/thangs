// Authenticate as admin
import PocketBase from 'pocketbase';

const pb = new PocketBase('http://127.0.0.1:8090');

const authData = await pb.admins.authWithPassword('adityamhegde@icloud.com', 'P@&^230rd');

// after the above we can access data from the authStore
console.log(pb.authStore.isValid);
console.log(pb.authStore.token);
console.log(pb.authStore.model.id);

// "logout" after the last authenticated account
pb.authStore.clear();

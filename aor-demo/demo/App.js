import React from 'react';
import { simpleRestClient, Admin, Resource } from 'admin-on-rest';
import { Delete } from 'admin-on-rest/lib/mui';

import { 
    PetList,
    PetShow
} from './Pet';
import { 
    UserList,
    UserShow
} from './User';
import { 
    OrderList,
    OrderShow
} from './Order';
import { 
    TagList,
    TagShow
} from './Tag';
import { 
    CategoryList,
    CategoryShow
} from './Category';


const App = () => (
    <Admin title={"demo"} restClient={simpleRestClient}>
        <Resource
            name={"Pet"}
            list={ PetList }
            show={ PetShow }
            remove={Delete}
        />
        <Resource
            name={"User"}
            list={ UserList }
            show={ UserShow }
            remove={Delete}
        />
        <Resource
            name={"Order"}
            list={ OrderList }
            show={ OrderShow }
            remove={Delete}
        />
        <Resource
            name={"Tag"}
            list={ TagList }
            show={ TagShow }
            remove={Delete}
        />
        <Resource
            name={"Category"}
            list={ CategoryList }
            show={ CategoryShow }
            remove={Delete}
        />
    </Admin>
)

export default App;
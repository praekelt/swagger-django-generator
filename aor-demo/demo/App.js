import React from 'react';
import { simpleRestClient, Admin, Resource } from 'admin-on-rest';
import { Delete } from 'admin-on-rest/lib/mui';

import { 
    UserList,
    UserShow
} from './User';
import { 
    CategoryList,
    CategoryShow
} from './Category';
import { 
    TagList,
    TagShow
} from './Tag';
import { 
    PetList,
    PetShow
} from './Pet';
import { 
    OrderList,
    OrderShow
} from './Order';


const App = () => (
    <Admin title={"demo"} restClient={simpleRestClient}>
        <Resource
            name={"User"}
            list={ UserList }
            show={ UserShow }
            remove={Delete}
        />
        <Resource
            name={"Category"}
            list={ CategoryList }
            show={ CategoryShow }
            remove={Delete}
        />
        <Resource
            name={"Tag"}
            list={ TagList }
            show={ TagShow }
            remove={Delete}
        />
        <Resource
            name={"Pet"}
            list={ PetList }
            show={ PetShow }
            remove={Delete}
        />
        <Resource
            name={"Order"}
            list={ OrderList }
            show={ OrderShow }
            remove={Delete}
        />
    </Admin>
)

export default App;
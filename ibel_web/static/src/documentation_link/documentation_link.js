/** @odoo-module **/

import { DocumentationLink } from "@web/views/widgets/documentation_link/documentation_link"
import {patch} from "@web/core/utils/patch";
import { session } from "@web/session";
const LINK_REGEX = new RegExp("^https?://");

// Changes Odoo to My Title in window title
patch(DocumentationLink.prototype,  {
    get url() {
        if (LINK_REGEX.test(this.props.path)) {
            return this.props.path;
        } else {
            const serverVersion = session.server_version_info.includes("final")
                ? `${session.server_version_info[0]}.${session.server_version_info[1]}`.replace(
                      "~",
                      "-"
                  )
                : "master";
            return "https://www.ibel.app/documentation/" + serverVersion + this.props.path;
        }
    }

});

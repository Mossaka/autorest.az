/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

import * as fs from 'fs';
import { EOL } from 'os';
import * as path from 'path';
import { isNullOrUndefined } from "util";
import { PathConstants } from '../../../models';
import { CodeModelAz } from "../../CodeModelAz";
import { HeaderGenerator } from "../../Header";
import { TemplateBase } from "../TemplateBase";

export class CliMainDocSourceJsonMap extends TemplateBase {
    constructor(model: CodeModelAz, isDebugMode: boolean) {
        super(model, isDebugMode);
        this.relativePath = path.join(model.AzureCliFolder, PathConstants.docSourceJsonFile);
    }

    public async fullGeneration(): Promise<string[]> {
        return this.GenerateDocSourceJsonMap(this.model, this.relativePath);
    }

    public async incrementalGeneration(base: string): Promise<string[]> {
        return null;
    }   

    private GenerateDocSourceJsonMap(model: CodeModelAz, docSourceJsonMapPath): string[] {
        let header: HeaderGenerator = new HeaderGenerator();
        let outputFile = fs.readFileSync(docSourceJsonMapPath).toString().split(EOL);
        let docSourceJson = require(docSourceJsonMapPath);
        if (isNullOrUndefined(docSourceJson[model.Extension_NameUnderscored])) {
            let line = '"' + model.Extension_Name + '": "src/azure-cli/azure/cli/command_modules/' + model.Extension_Name + '/_help.py"';
            let cnt = outputFile.length;
            let foundLastLine = false;
            while (cnt > 0) {
                cnt--;
                if (outputFile[cnt][0] == "}") {
                    foundLastLine = true;
                    continue;
                }
                if (foundLastLine) {
                    let len = outputFile[cnt].length;
                    if (outputFile[cnt][len - 1] == '\r') {
                        outputFile[cnt] = outputFile[cnt].replace('\r', ',');
                    } else {
                        outputFile[cnt] += ",";
                    }
                    let indexSize = outputFile[cnt].indexOf('"');
                    outputFile.splice(cnt + 1, 0, " ".repeat(indexSize) + line);
                    break;
                }
            }
        }
        return outputFile;
    }
}